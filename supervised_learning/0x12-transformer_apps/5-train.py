'''Train Transformer module

   Software version:
    - python3 (version 3.6.12)
    - numpy (version 1.16)
    - tensorflow (version 2.4.1)
    - pycodestyle (version 2.4)

   Heavily based on: https://www.tensorflow.org/text/tutorials/
             transformer#training_and_checkpointing
'''
import tensorflow.compat.v2 as tf
Dataset = __import__('3-dataset').Dataset
create_masks = __import__('4-create_masks').create_masks
Transformer = __import__('5-transformer').Transformer


tf.config.run_functions_eagerly(True)


def train_transformer(N, dm, h, hidden, max_len, batch_size, epochs):
    '''creates and trains a transformer model for machine translation of
       Portuguese to English
    Args:
        N the number of blocks in the encoder and decoder
        dm the dimensionality of the model
        h the number of heads
        hidden the number of hidden units in the fully connected layers
        max_len the maximum number of tokens per sequence
        batch_size the batch size for training
        epochs the number of epochs to train for

    Important:
        - The model will  be trained with Adam optimization with
          beta_1=0.9, beta_2=0.98, epsilon=1e-9 and custom learning
          rate
        - The model will use sparse categorical crossentropy loss, ignoring
          padded tokens
        - Every 50 batches, will print: Epoch {Epoch number}, batch
          {batch_number}: loss {training_loss} accuracy {training_accuracy}
        - Every epoch, will print: Epoch {Epoch number}: loss {training_loss}
          accuracy {training_accuracy}

    Returns: the trained model
    '''
    dataset = Dataset(batch_size, max_len)

    transformer = Transformer(
        N=N,
        dm=dm,
        h=h,
        hidden=hidden,
        input_vocab=dataset.tokenizer_pt.vocab_size + 2,
        target_vocab=dataset.tokenizer_en.vocab_size + 2,
        max_seq_input=max_len,
        max_seq_target=max_len,
    )

    custom_LR = CustomLRSchedule(dm)

    optimizer = tf.keras.optimizers.Adam(
        learning_rate=custom_LR,
        beta_1=0.9,
        beta_2=0.98,
        epsilon=1e-9,
    )

    # --- Calculate Loss and Metrics ---
    loss_object = tf.keras.losses.SparseCategoricalCrossentropy(
        from_logits=True,
        reduction='none',
    )

    # to ignore the padded tokens for the loss, :
    def loss_function(real, pred):
        '''custom loss function that masks tokens
        Args:
            real the real tokens
            pred the predicted tokens

        Returns: tensor with the calculated loss
        '''
        mask = tf.math.logical_not(tf.math.equal(real, 0))
        loss_ = loss_object(real, pred)

        mask = tf.cast(mask, dtype=loss_.dtype)
        loss_ *= mask

        return tf.reduce_sum(loss_)/tf.reduce_sum(mask)

    train_loss = tf.keras.metrics.Mean(name='train_loss')
    train_accuracy = tf.keras.metrics.Mean(name='train_accuracy')

    # to ignore the padded tokens for the metrics:
    def accuracy_function(real, pred):
        '''custom accuracy function that masks tokens
            real the real tokens
            pred the predicted tokens

        Returns: tensor with the calculated accuracy
        '''

        accuracies = tf.equal(real, tf.argmax(pred, axis=2))

        mask = tf.math.logical_not(tf.math.equal(real, 0))
        accuracies = tf.math.logical_and(mask, accuracies)

        accuracies = tf.cast(accuracies, dtype=tf.float32)
        mask = tf.cast(mask, dtype=tf.float32)

        return tf.reduce_sum(accuracies)/tf.reduce_sum(mask)
    # -------------------------------------

    # ------------------- CUSTOM TRAIN STEP -----------------------
    # This section heavily extracted from https://www.tensorflow.org/text/
    #     tutorials/transformer#training_and_checkpointing

    # The @tf.function trace-compiles train_step into a TF graph for faster
    # execution. The function specializes to the precise shape of the argument
    # tensors. To avoid re-tracing due to the variable sequence lengths or
    # variable batch sizes (the last batch is smaller), use input_signature to
    # specify more generic shapes.

    train_step_signature = [
        tf.TensorSpec(shape=(None, None), dtype=tf.int64),
        tf.TensorSpec(shape=(None, None), dtype=tf.int64),
    ]

    @tf.function(input_signature=train_step_signature)
    def train_step(inp, tar):
        tar_inp = tar[:, :-1]
        tar_real = tar[:, 1:]

        enc_mask, look_ah_mask, dec_mask = create_masks(inp, tar_inp)

        with tf.GradientTape() as tape:
            predictions = transformer(
                inp,
                tar_inp,
                True,
                enc_mask,
                look_ah_mask,
                dec_mask,
            )
            loss = loss_function(tar_real, predictions)

        gradients = tape.gradient(loss, transformer.trainable_variables)
        optimizer.apply_gradients(zip(
            gradients,
            transformer.trainable_variables,
        ))

        train_loss(loss)
        train_accuracy(accuracy_function(tar_real, predictions))
    # -------------------------------------------------------------

    # ----------------------- TRAINING ----------------------------
    for epoch in range(epochs):
        train_loss.reset_states()
        train_accuracy.reset_states()

        # inp -> portuguese, tar -> english
        for (batch, (inp, tar)) in enumerate(dataset.data_train):
            train_step(inp, tar)

            if batch % 50 == 0:
                print(("Epoch {}, batch {}: " +
                      "loss {} accuracy {}").format(
                          epoch + 1,
                          batch,
                          train_loss.result(),
                          train_accuracy.result(),
                      ))

        print("Epoch {}: loss {} accuracy {}".format(
            epoch + 1,
            train_loss.result(),
            train_accuracy.result(),
        ))
    # -------------------------------------------------------------

    return transformer


class CustomLRSchedule(tf.keras.optimizers.schedules.LearningRateSchedule):
    '''creates a custom Larning Rate Schedule'''

    def __init__(self, dm, warmup_steps=4000):
        '''CustomLRSchedule class constructor
        Args:
            dm the dimensionality of the model
            warmup_steps are the number of updates with low learning rate
        '''
        super(CustomLRSchedule, self).__init__()

        self.dm = dm
        self.dm = tf.cast(self.dm, tf.float32)
        self.warmup_steps = warmup_steps

    def __call__(self, step):
        '''Instantiation
        Args:
            step is the number of regular steps

        Returns: The Learning Rate
        '''
        part_a = tf.math.rsqrt(step)
        part_b = step * (self.warmup_steps ** -1.5)

        return tf.math.rsqrt(self.dm) * tf.math.minimum(part_a, part_b)

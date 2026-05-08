class SimpleConnTrigger:
    def __enter__(self):
        print("Entering the connection context...")
        # Here you can add code to establish a connection or perform setup tasks.
        return self
    def __exit__(self, exc_type, exc_value, exc_tb):
        print('Exiting the connection context properly...')

        if exc_type is not None:
            print(f'An exception occurred: {exc_type}, {exc_value}')

conn = SimpleConnTrigger()
with conn as cs:
    print("Inside the connection context.")
    # Here you can add code to perform operations while the connection is active.

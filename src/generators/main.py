from generators import incremental_counter, timeout_iterator

def main():
    print("starting incremental counter..")
    print("running for 5 seconds..")

    gen = incremental_counter()
    timeout_iterator(gen, 5)

    print("done.")

if __name__ == "__main__":
    main()
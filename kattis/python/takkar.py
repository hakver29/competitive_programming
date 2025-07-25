def main():
    trump_button = int(input())
    kim_button = int(input())

    if trump_button > kim_button:
        print("MAGA!")
    elif trump_button < kim_button:
        print("FAKE NEWS!")
    else:
        print("WORLD WAR 3!")

if __name__ == "__main__":
    main()

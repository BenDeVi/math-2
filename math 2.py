def fraction():
    while True:
        try:
            x, y = map(int, input("Fraction: ").split('/'))
            if x > y or y == 0:
                raise ValueError
            return x, y
        except ValueError:
            pass

# _ is percent rember that

def main():
    
    x, y = fraction()
    _ = (x / y) * 100
    print("E" if _ <= 1

          else "F" if _ >= 99
          else f"{round(_)}%")

if __name__ == "__main__":

    main()

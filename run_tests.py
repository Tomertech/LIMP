

def main():
    print("HERE")
    loss = optimize_intep(vae, interp_loader, opt, 0, 1e1)
    print(loss)
    print("HERE2")


if __name__ == "__main__":
        main()
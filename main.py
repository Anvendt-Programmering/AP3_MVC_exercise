from controller import Controller
from views import View
from models import Model


def main():
    print("Hello, MVC!")
    model = Model()
    view = View()
    controller = Controller(model, view)
    view.set_controller(controller)
    model.set_controller(controller)

    # event loop etc.
    while True:
        value = controller.update()
        if value == "0":
            break


if __name__ == "__main__":
    main()

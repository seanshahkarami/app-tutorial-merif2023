import numpy as np
from waggle.data.vision import Camera
from waggle.plugin import Plugin


def compute_mean_color(image):
    return np.mean(image, (0, 1)).astype(float)


def main():
    with Plugin() as plugin:
        # read example image from file
        with Camera("left") as camera:
            snapshot = camera.snapshot()

        print(snapshot)

        # compute mean color
        mean_color = compute_mean_color(snapshot.data)

        # print mean color
        print(mean_color)

        plugin.publish("image.mean.r", mean_color[0], timestamp=snapshot.timestamp)
        plugin.publish("image.mean.g", mean_color[1], timestamp=snapshot.timestamp)
        plugin.publish("image.mean.b", mean_color[2], timestamp=snapshot.timestamp)

        snapshot.save("sample.jpg")
        plugin.upload_file("sample.jpg", timestamp=snapshot.timestamp)


if __name__ == "__main__":
    main()

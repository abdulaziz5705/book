import uuid


class Save(object):

    def save_image(instance, filename):
        image_path = filename.split(",")[-1]
        return f"book/{uuid.uuid4()}.{image_path}"

    def save_image_path(instance, filename):
        image_path = filename.split(",")[-1]
        return f"author/{uuid.uuid4()}.{image_path}"

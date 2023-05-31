from pathlib import Path
import base64


def img2bytes(path):
    img_bytes = Path(path).read_bytes()
    return base64.b64encode(img_bytes).decode()


MODEL_TIFUKNN = "TIFU KNN"
MODEL_POPULAR = "Popularity-based"

ITEM_IMG_WIDTH = 175

ITEMS_AMOUNT = 60
ITEMS_PER_ROW = 5

DEFAULT_ITEMS_AMOUNT = 3

ITEMS_MAPPING = "../data/item_mapping.json"

# исторические данные с покупками клиентов
purchase_data = "../data/main.csv"

# предобработанный датасет для tifu knn (!!! находится в архиве -> распаковать !!!)
users_as_vectors = "../data/users_as_vectors.pkl"

REPO_LINK = "https://github.com/exsandebest/next-basket-recommendation"

HTML_CREDITS = \
    """[<img src='data:image/png;base64,{0}' class='img-fluid' width=25 height=25>]({1}) <small> Demo stand | Team 42 </small>""" \
    .format(img2bytes("../images/github_logo.png"), REPO_LINK)


# Stubs
DATA_PATH = "../data/apriori_top_20.csv"
RAND_IMAGE = "https://picsum.photos/200/300"
DESCRIPTION = "Next basket recomendation model"

# отдельно заданы средние метрики на валидации для базового алгоритма - popular и доп. алгоритмов (сейчас только tifu)
# все алгоритмы сравниваются с базой:
# например, для tifu current_f1 - метрика tifu, prev_f1 - метрика popular

TIFU_METRICS = { "current_f1": 0.39744, "prev_f1": 0.37593 }
POPULAR_METRICS = { "current_f1": 0.37593, "prev_f1": 0.37593 }
import fire
from near.api import NearAPI


class main:
    fire.Fire(NearAPI(), name="near-api")
    # near_api = NearAPI()


if __name__ == "__main__":
    main()

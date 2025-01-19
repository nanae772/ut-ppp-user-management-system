import dataclasses
import enum


class データベース:
    pass


class メッセージバス:
    pass


class 前提条件:
    @staticmethod
    def 要求(条件: bool):
        if not 条件:
            raise Exception(f"前提条件を満たしていません: {条件=}")


class ユーザ型(enum.Enum):
    顧客 = enum.auto()
    従業員 = enum.auto()


@dataclasses.dataclass
class メールアドレス変更イベント:
    ユーザid: int
    新しいメールアドレス: str


class 会社:
    def __init__(self, ドメイン名: str, 従業員数: int):
        self.ドメイン名 = ドメイン名
        self.従業員数 = 従業員数

    def 従業員数を変更(self, 差分: int):
        前提条件.要求(self.従業員数 + 差分 >= 0)

        self.従業員数 += 差分

    def 会社のドメインである(self, メールアドレス: str) -> bool:
        メールドメイン = メールアドレス.split("@")[1]
        return self.ドメイン名 == メールドメイン


class ユーザ:
    def __init__(self, ユーザid: int, Eメール: str, タイプ: ユーザ型):
        self.ユーザId = ユーザid
        self.メールアドレス = Eメール
        self.タイプ = タイプ
        self.メールアドレス変更イベントリスト: list[メールアドレス変更イベント] = []

    def メールアドレスを変更(self, 新メールアドレス: str, a会社: 会社) -> None:
        if self.メールアドレス == 新メールアドレス:
            return

        新しいタイプ = (
            ユーザ型.従業員
            if a会社.会社のドメインである(新メールアドレス)
            else ユーザ型.顧客
        )

        if self.タイプ != 新しいタイプ:
            差分 = 1 if 新しいタイプ == ユーザ型.従業員 else -1
            a会社.従業員数を変更(差分)

        self.メールアドレス = 新メールアドレス
        self.タイプ = 新しいタイプ
        self.メールアドレス変更イベントリスト.append(
            メールアドレス変更イベント(self.ユーザId, 新メールアドレス)
        )


class ユーザファクトリ:
    @staticmethod
    def 作成(データ):
        前提条件.要求(len(データ) >= 3)

        ユーザid = データ[0]
        メールアドレス = データ[1]
        タイプ = データ[2]

        return ユーザ(ユーザid, メールアドレス, タイプ)


class 会社ファクトリ:
    @staticmethod
    def 作成(データ):
        前提条件.要求(len(データ) >= 2)
        会社のドメイン名 = データ[0]
        従業員数 = データ[1]
        return 会社(会社のドメイン名, 従業員数)


class ユーザコントローラ:
    def __init__(self):
        self._データベース = データベース()
        self._メッセージバス = メッセージバス()

    def メールアドレスを変更(self, ユーザid: int, 新メールアドレス: str):
        ユーザデータ = self._データベース.idでユーザを取得(ユーザid)
        aユーザ = ユーザファクトリ.作成(ユーザデータ)

        会社データ = self._データベース.会社を取得()
        a会社 = 会社ファクトリ.作成(会社データ)

        aユーザ.メールアドレスを変更(新メールアドレス, a会社)

        self._データベース.会社情報を保存(a会社)
        self._データベース.ユーザ情報を保存(aユーザ)
        for イベント in aユーザ.メールアドレス変更イベントリスト:
            self._メッセージバス.メールアドレス変更メッセージを送信(
                イベント.ユーザid, イベント.新しいメールアドレス
            )

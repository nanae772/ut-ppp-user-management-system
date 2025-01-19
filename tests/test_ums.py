from ut_ppp_ums_example.main import 会社, ユーザ, ユーザ型


class Testユーザクラス:
    def test_非従業員から従業員のメールアドレスに変更(self):
        a会社 = 会社("mycorp.com", 1)
        テスト対象 = ユーザ(1, "user@gmail.com", ユーザ型.顧客)

        テスト対象.メールアドレスを変更("new@mycorp.com", a会社)

        assert a会社.従業員数 == 2
        assert テスト対象.メールアドレス == "new@mycorp.com"
        assert テスト対象.タイプ == ユーザ型.従業員

    def test_従業員から非従業員のメールアドレスに変更(self):
        a会社 = 会社("mycorp.com", 1)
        テスト対象 = ユーザ(1, "user@mycorp.com", ユーザ型.従業員)

        テスト対象.メールアドレスを変更("new@gmail.com", a会社)

        assert a会社.従業員数 == 0
        assert テスト対象.メールアドレス == "new@gmail.com"
        assert テスト対象.タイプ == ユーザ型.顧客

    def test_ユーザのタイプを変えずにメールアドレスを変更(self):
        a会社 = 会社("mycorp.com", 1)
        テスト対象 = ユーザ(1, "user@gmail.com", ユーザ型.顧客)

        テスト対象.メールアドレスを変更("new@yahoo.co.jp", a会社)

        assert a会社.従業員数 == 1
        assert テスト対象.メールアドレス == "new@yahoo.co.jp"
        assert テスト対象.タイプ == ユーザ型.顧客

    def test_メールアドレスを同じメールアドレスに変更(self):
        a会社 = 会社("mycorp.com", 1)
        テスト対象 = ユーザ(1, "user@gmail.com", ユーザ型.顧客)

        テスト対象.メールアドレスを変更("user@gmail.com", ユーザ型.顧客)

        assert a会社.従業員数 == 1
        assert テスト対象.メールアドレス == "user@gmail.com"
        assert テスト対象.タイプ == ユーザ型.顧客

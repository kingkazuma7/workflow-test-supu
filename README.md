# Workflow Test

シンプルなPythonプロジェクトのテンプレート。GitHub Actionsで自動テスト実行。

## 構成

- `src/add.py` - 足し算関数の実装
- `tests/test_add.py` - ユニットテスト（pytest）
- `requirements.txt` - 依存関係（pytest）
- `.github/workflows/test.yml` - PR時の自動テスト実行

## 使い方

### ローカルでテスト実行

```bash
pip install -r requirements.txt
pytest tests/
```

### PR作成

PRを作成するとGitHub Actionsが自動でテストを実行します。テスト失敗時はPRがマージできません。

## 開発

新しい関数は `src/` 配下に追加し、対応するテストを `tests/` 配下に追加してください。

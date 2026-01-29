# streamlit-llm-app

AI専門家チャットアプリケーション - LangChainとOpenAI APIを使用した専門分野別チャットボット

## 📋 機能

- 🎓 4種類の専門家（医療、プログラミング、ビジネス、教育）から選択可能
- 💬 LangChainを使用したLLM連携
- 🎯 選択した専門分野に応じたシステムメッセージの切り替え
- 🖥️ Streamlitによる直感的なUI

## 🚀 セットアップ

### 1. リポジトリのクローン

```bash
git clone <your-repo-url>
cd streamlit-llm-app
```

### 2. 仮想環境の作成とアクティベート

```bash
python -m venv env
# Windows
env\Scripts\activate
# Mac/Linux
source env/bin/activate
```

### 3. 依存パッケージのインストール

```bash
pip install -r requirements.txt
```

### 4. 環境変数の設定

`.env`ファイルを作成し、OpenAI APIキーを設定：

```bash
OPENAI_API_KEY=your_openai_api_key_here
```

### 5. アプリの起動

```bash
streamlit run app.py
```

## 🌐 Streamlit Community Cloudへのデプロイ

1. GitHubにリポジトリをプッシュ
2. [Streamlit Community Cloud](https://streamlit.io/cloud)にアクセス
3. リポジトリを選択してデプロイ
4. Secrets設定で`OPENAI_API_KEY`を追加

Pythonバージョンは`.python-version`ファイルで3.11に設定されています。

## 📝 使い方

1. サイドバーから専門家を選択
2. テキストエリアに質問を入力
3. 送信ボタンをクリック
4. 選択した専門家からの回答を確認

## 🛠️ 技術スタック

- **Streamlit**: Webアプリケーションフレームワーク
- **LangChain**: LLMアプリケーション開発フレームワーク
- **OpenAI API**: GPT-3.5-turbo モデル
- **Python**: 3.11

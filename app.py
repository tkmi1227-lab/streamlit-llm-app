import streamlit as st      
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

# 環境変数を読み込む
load_dotenv()

# ページ設定
st.set_page_config(
    page_title="AI専門家チャットアプリ",
    page_icon="🎓",
    layout="wide"
)

# LLMモデルを初期化
@st.cache_resource
def load_llm():
    return ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0.5
    )

def get_expert_prompt(expert_type: str) -> str:
    """専門家の種類に応じたシステムメッセージを返す"""
    expert_prompts = {
        "医療専門家": "あなたは経験豊富な医療専門家です。医学的な知識を持ち、健康や医療に関する質問に対して、専門的かつ分かりやすく回答してください。ただし、診断や治療の推奨は行わず、一般的な情報提供に留めてください。",
        "プログラミング専門家": "あなたは熟練したプログラミング専門家です。様々なプログラミング言語やフレームワークに精通しており、コードの書き方、デバッグ、ベストプラクティスについて詳しく説明できます。具体的なコード例を交えて回答してください。",
        "ビジネスコンサルタント": "あなたは経験豊富なビジネスコンサルタントです。経営戦略、マーケティング、組織運営などのビジネス課題に対して、実践的なアドバイスと具体的なソリューションを提供してください。",
        "教育アドバイザー": "あなたは教育分野の専門家です。学習方法、教育理論、キャリア開発について深い知識を持ち、学習者の成長をサポートする具体的なアドバイスを提供してください。"
    }
    return expert_prompts.get(expert_type, "")

def get_llm_response(user_input: str, expert_type: str) -> str:
    """
    入力テキストと専門家の種類を受け取り、LLMからの回答を返す
    
    Args:
        user_input: ユーザーからの入力テキスト
        expert_type: 選択された専門家の種類
    
    Returns:
        LLMからの回答テキスト
    """
    try:
        llm = load_llm()
        
        # システムメッセージを取得
        system_prompt = get_expert_prompt(expert_type)
        
        # プロンプトを構築
        prompt = f"{system_prompt}\n\nユーザーの質問: {user_input}"
        
        # LLMに送信
        response = llm.invoke(prompt)
        return response.content
        
    except Exception as e:
        return f"エラーが発生しました: {str(e)}\n\n環境変数 OPENAI_API_KEY が正しく設定されていることを確認してください。"

# アプリのタイトルと説明
st.title("🎓 AI専門家チャットアプリ")

st.markdown("""
## 📖 アプリの概要
このアプリは、様々な分野の専門家として振る舞うAIとチャットができるアプリケーションです。
LangChainとOpenAI APIを使用して、選択した専門分野に応じた回答を提供します。

## 🚀 使い方
1. **専門家を選択**: 下のラジオボタンから相談したい専門家を選択してください
2. **質問を入力**: テキストエリアに質問や相談内容を入力してください
3. **送信**: 「送信」ボタンをクリックすると、選択した専門家として回答が生成されます

---
""")

# サイドバーに専門家選択を配置
with st.sidebar:
    st.header("⚙️ 設定")
    expert_type = st.radio(
        "専門家を選択してください:",
        options=[
            "医療専門家",
            "プログラミング専門家",
            "ビジネスコンサルタント",
            "教育アドバイザー"
        ],
        index=1,
        help="質問内容に合わせて専門家を選択してください"
    )
    
    st.markdown("---")
    st.markdown(f"**現在の選択**: {expert_type}")
    
    # 選択された専門家の説明を表示
    expert_descriptions = {
        "医療専門家": "健康や医療に関する一般的な情報を提供します",
        "プログラミング専門家": "コードやプログラミングの技術的な質問に回答します",
        "ビジネスコンサルタント": "ビジネス戦略や経営に関するアドバイスを提供します",
        "教育アドバイザー": "学習方法や教育に関するサポートを提供します"
    }
    st.info(expert_descriptions[expert_type])

# メインコンテンツ
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader(f"💬 {expert_type}に質問する")

# 入力フォーム
with st.form(key="input_form"):
    user_input = st.text_area(
        "質問を入力してください",
        height=200,
        placeholder="ここに質問や相談内容を入力してください...",
        help="具体的な質問をすると、より詳しい回答が得られます"
    )
    submit_button = st.form_submit_button(
        "📤 送信",
        use_container_width=True
    )

# 送信ボタンが押されたときの処理
if submit_button:
    if user_input.strip():
        with st.spinner(f"{expert_type}が回答を生成中..."):
            # 関数を使ってLLMからの回答を取得
            response = get_llm_response(user_input, expert_type)
            
            # 回答を表示
            st.success("✅ 回答が生成されました")
            
            st.markdown("### 📝 質問:")
            st.info(user_input)
            
            st.markdown(f"### 💡 {expert_type}からの回答:")
            st.markdown(response)
            
    else:
        st.warning("⚠️ 質問を入力してください。")

# フッター
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: gray; font-size: 0.8em;'>
    Powered by LangChain & OpenAI API
</div>
""", unsafe_allow_html=True)

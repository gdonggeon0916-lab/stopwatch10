from pathlib import Path
import streamlit as st
import streamlit.components.v1 as components

# 페이지 기본 설정
st.set_page_config(
    page_title="Smart 집중 스톱워치",
    page_icon="⏱️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# HTML 파일 경로 설정 (상대 경로)
HTML_FILE_PATH = Path(__file__).resolve().parent / "htmls" / "index.html"


def main():
    # 메인 헤더 안내
    st.title("⏱️ Smart 집중 스톱워치")
    st.caption(
        "목표를 설정하고 효율적으로 시간을 측정하여 학습 결과를 관리해보세요."
    )
    st.markdown("---")

    # index.html 파일 존재 확인 및 렌더링
    if not HTML_FILE_PATH.exists():
        st.error("⚠️ `htmls/index.html` 파일을 찾을 수 없습니다.")
        st.info(
            "프로젝트 폴더 내 `htmls/` 디렉터리에 `index.html` 파일이 위치해 있는지 확인해 주세요."
        )
        return

    try:
        with open(HTML_FILE_PATH, "r", encoding="utf-8") as f:
            html_content = f.read()

        # HTML 컴포넌트 출력
        components.html(html_content, height=850, scrolling=True)

    except Exception as e:
        st.error(f"⚠️ HTML 파일을 읽는 도중 오류가 발생했습니다: {e}")


if __name__ == "__main__":
    main()
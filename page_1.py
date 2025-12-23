import streamlit as st
import streamlit.components.v1 as components

from pyodide.http import pyfetch  # 用于从Python调用HTTP请求的示例函数
from pyodide_js import pyodide_to_js  # 用于在Python和JS之间转换数据的函数
from pyodide import JSBinOp  # 用于在JS和Python之间传递数据的装饰器

st.title("Page 1")

st.title("🎈 Google")
# st.write(
#    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
# )

components.iframe("https://sv.kesug.com/index.php", height=800)

# 定义一个简单的JS函数，它将与Python交互
js_code = """
function interactWithPython() {
    // 一些JavaScript逻辑...
    console.log("JavaScript called Python!");
    // 使用JSBinOp装饰器从JS调用Python函数
    const result = pyodide.runPython(`1 + 1`);  // 调用Python代码并获取结果
    console.log("Result from Python:", result);  // 在控制台中打印结果
}
"""
pyodide_to_js(js_code)()  # 执行JS代码以初始化交互功能

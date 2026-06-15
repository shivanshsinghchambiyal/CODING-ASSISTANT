import pyautogui
import pytesseract
import pygetwindow as gw
from PIL import Image

# Tesseract Path
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


def take_screenshot():

    try:
        chrome = gw.getWindowsWithTitle("LeetCode")[0]

        left = chrome.left
        top = chrome.top
        width = chrome.width
        height = chrome.height

        img = pyautogui.screenshot(
            region=(left, top, width, height)
        )

    except:
        # Fallback
        img = pyautogui.screenshot()

    img.save("screen.png")


def extract_text():

    text = pytesseract.image_to_string(
        Image.open("screen.png")
    )

    return text.lower()


# ==========================
# LEETCODE ANALYZER
# ==========================

def detect_pattern(text):

    if "substring" in text:
        return {
            "Pattern": "Sliding Window",
            "Complexity": "O(n)",
            "Hint": "Maintain a window of unique characters."
        }

    elif "sorted array" in text:

        return {
            "Pattern": "Two Pointer / Binary Search",
            "Complexity": "O(n) or O(log n)",
            "Hint": "Use sorted property."
        }

    elif "tree" in text:

        return {
            "Pattern": "Tree Traversal",
            "Complexity": "Depends on traversal"
        }

    elif "graph" in text:

        return {
            "Pattern": "Graph",
            "Complexity": "O(V+E)"
        }

    elif "longest common subsequence" in text:

        return {
            "Pattern": "Dynamic Programming",
            "Complexity": "O(n*m)"
        }

    return {
        "Pattern": "Unknown",
        "Hint": "Try brute force first."
    }


# ==========================
# ERROR ANALYZER
# ==========================

def analyze_error(text):

    if "no matching function for call to" in text:

        return {
            "Error Type": "Type Mismatch",

            "Explanation":
            "Function arguments do not match expected datatype.",

            "Why":
            "You are passing the wrong datatype.",

            "Suggested Fix":
            "Check parameter types carefully.",

            "Confidence":
            "90%",

            "Similar Mistakes":
            """
            push_back("abc") in vector<int>
            assigning string to int
            storing char* in vector<int>
            """
        }

    elif "expected ';'" in text:

        return {
            "Error Type": "Syntax Error",

            "Explanation":
            "Missing semicolon.",

            "Why":
            "Every statement must end with ';'.",

            "Suggested Fix":
            "Add ';' at the end of statement.",

            "Confidence":
            "99%"
        }

    elif "was not declared in this scope" in text:

        return {
            "Error Type": "Declaration Error",

            "Explanation":
            "Variable or function not declared.",

            "Why":
            "Compiler cannot find the identifier.",

            "Suggested Fix":
            "Declare variable before use.",

            "Confidence":
            "95%"
        }

    elif "segmentation fault" in text:

        return {
            "Error Type": "Runtime Error",

            "Explanation":
            "Invalid memory access.",

            "Why":
            "Null pointer or out-of-bounds access.",

            "Suggested Fix":
            "Check pointers and array indices.",

            "Confidence":
            "90%"
        }

    return {
        "Error Type": "Unknown",
        "Explanation": "Could not identify the error."
    }


# ==========================
# MAIN
# ==========================

def main():

    take_screenshot()

    text = extract_text()

    print("\n========== OCR TEXT ==========\n")
    print(text[:3000])
    print("\n==============================\n")

    if "error:" in text or "compile error" in text:

        print("\n===== ERROR ANALYSIS =====\n")

        result = analyze_error(text)

        for key, value in result.items():
            print(f"{key}:")
            print(value)
            print()

    else:

        print("\n===== PROBLEM ANALYSIS =====\n")

        result = detect_pattern(text)

        for key, value in result.items():
            print(f"{key}:")
            print(value)
            print()


main()
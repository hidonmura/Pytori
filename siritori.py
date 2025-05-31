import ast
import builtins

class BuiltinFunctionVisitor(ast.NodeVisitor):
    def __init__(self):
        self.builtin_calls = []

    def visit_Call(self, node):
        # 関数呼び出しが ast.Name 型であることを確認
        if isinstance(node.func, ast.Name):
            func_name = node.func.id
            # 組み込み関数の名前と一致するかを確認
            if func_name in dir(builtins):
                self.builtin_calls.append((func_name, node.lineno))
        self.generic_visit(node)

def analyze_builtin_functions(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        code = file.read()
    tree = ast.parse(code, filename=file_path)
    visitor = BuiltinFunctionVisitor()
    visitor.visit(tree)
    return visitor.builtin_calls

# 使用例
if __name__ == "__main__":
    target_file = '1_hoge.py'  # 解析対象のPythonファイル名
    builtin_usages = analyze_builtin_functions(target_file)
    if builtin_usages:
        print(f"ファイル '{target_file}' で使用されている組み込み関数:")
        for func_name, lineno in builtin_usages:
            print(f"  行 {lineno}: {func_name}()")
    else:
        print(f"ファイル '{target_file}' で組み込み関数の使用は見つかりませんでした。")

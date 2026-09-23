"""
Leibniz 公式求 π 近似值
π/4 = 1 - 1/3 + 1/5 - 1/7 + ...

该模块可以独立运行，也提供了可被其他文件 import 的函数 compute_pi。
"""


def compute_pi(n_terms):
    """
    使用 Leibniz 公式计算 π 的近似值。

    参数:
        n_terms (int): 级数展开的项数（应 >= 1）

    返回:
        float: π 的近似值
    """
    if n_terms < 1:
        raise ValueError("n_terms 必须为正整数")

    total = 0.0
    sign = 1.0
    for i in range(n_terms):
        total += sign / (2 * i + 1)
        sign = -sign
    return total * 4


if __name__ == "__main__":
    n = 1000000
    pi_approx = compute_pi(n)
    print(f"[Leibniz] 项数 n = {n}")
    print(f"[Leibniz] π ≈ {pi_approx:.15f}")
    print(f"[Leibniz] 误差 = {abs(pi_approx - 3.141592653589793):.15f}")

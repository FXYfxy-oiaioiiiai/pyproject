"""
Euler 乘积公式求 π 近似值
π^2/6 = 1 + 1/4 + 1/9 + 1/16 + ... + 1/n^2

该模块可以独立运行，也提供了可被其他文件 import 的函数 compute_pi。
"""

import math


def compute_pi(n_terms):
    """
    使用 Euler 乘积公式（巴塞尔问题）计算 π 的近似值。

    参数:
        n_terms (int): 级数展开的项数（应 >= 1）

    返回:
        float: π 的近似值
    """
    if n_terms < 1:
        raise ValueError("n_terms 必须为正整数")

    total = 0.0
    for i in range(1, n_terms + 1):
        total += 1.0 / (i * i)
    return math.sqrt(6.0 * total)


if __name__ == "__main__":
    n = 1000000
    pi_approx = compute_pi(n)
    print(f"[Euler] 项数 n = {n}")
    print(f"[Euler] π ≈ {pi_approx:.15f}")
    print(f"[Euler] 误差 = {abs(pi_approx - 3.141592653589793):.15f}")

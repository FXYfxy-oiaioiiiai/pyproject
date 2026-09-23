"""
Ramanujan 公式求 π 近似值

1/π = (√8 / 99^2) * Σ_{n=0}^{∞} (4n)! * (1103 + 26390n) / ( n!^4 * 396^(4n) )

该模块可以独立运行，也提供了可被其他文件 import 的函数 compute_pi。
Ramanujan 公式收敛极快，很少的项数即可得到极高精度。
"""

import math


def compute_pi(n_terms):
    """
    使用 Ramanujan 公式计算 π 的近似值。

    参数:
        n_terms (int): 级数求和的项数（从 n=0 到 n=n_terms-1）
                       通常 n_terms = 1 或 2 即可达到机器精度。

    返回:
        float: π 的近似值
    """
    if n_terms < 1:
        raise ValueError("n_terms 必须为正整数")

    total = 0.0
    for n in range(n_terms):
        num = math.factorial(4 * n) * (1103 + 26390 * n)
        den = (math.factorial(n) ** 4) * (396 ** (4 * n))
        total += num / den

    return 1.0 / ((math.sqrt(8) / (99 ** 2)) * total)


if __name__ == "__main__":
    n = 1
    pi_approx = compute_pi(n)
    print(f"[Ramanujan] 项数 n = {n}")
    print(f"[Ramanujan] π ≈ {pi_approx:.15f}")
    print(f"[Ramanujan] 误差 = {abs(pi_approx - 3.141592653589793):.15f}")

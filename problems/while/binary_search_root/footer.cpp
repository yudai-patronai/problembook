



int main()
{
    std::string func_str;
    std::cin >> func_str;
    double a, b, tol, true_root;
    std::cin >> a >> b >> tol >> true_root;
    eps = 1e-6
    exec(func_str)
    root = find_root(f, a, b, tol)

}



if abs(f(root)) < eps or abs(root - true_root) < tol:
    print('YES')
else:
    print('NO')

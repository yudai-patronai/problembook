double lin(double x){
  return x + 0.1;
}

double quad(double x){
  return x * x + 5.0 * x;
}

double cub_1(double x){
  return x * x * x - 0.9;
}

double cub_2(double x){
  return x * x * x - 0.5;
}

double cub_3(double x){
  return x * x * x - 0.2;
}

int main()
{
    std::string func_str;
    std::cin >> func_str;
    double a, b, tol, true_root;
    std::cin >> a >> b >> tol >> true_root;
    double (*func)(double);
    if(func_str == "lin")
      func = lin;
    if(func_str == "quad")
      func = quad;
    if(func_str == "cub_1")
      func = cub_1;
    if(func_str == "cub_2")
      func = cub_2;
    if(func_str == "cub_3")
      func = cub_3;
    double root = find_root(func, a, b, tol);
    if(abs(root - true_root) < tol)
      std::cout << "YES" << std::endl;
    else
      std::cout << "NO" << std::endl;
    return 0;
}

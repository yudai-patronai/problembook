#include <iostream>
#include <string>

int poschitat_zarplatu_sotrudnika();

bool detect_nachalnik(std::string nomer_avtomobilya);

int poschitat_shtraf(std::string nomer_avtomobilya);

bool krutoj_nomer(std::string nomer_avtomobilya);

bool krasivyj_nomer(std::string nomer_avtomobilya);

int main()
{
  int zarplata = poschitat_zarplatu_sotrudnika();
  std::cout << zarplata << std::endl;

  return EXIT_SUCCESS;
}

int poschitat_zarplatu_sotrudnika()
{
  int summa_shtrafov = 0;
  int skorost_avtomobilya;
  std::string nomer_avtomobilya;

  std::cin >> skorost_avtomobilya >> nomer_avtomobilya;

  while (!detect_nachalnik(nomer_avtomobilya))
  {
    if (skorost_avtomobilya > 60)
    {
      summa_shtrafov += poschitat_shtraf(nomer_avtomobilya);
    }

    std::cin >> skorost_avtomobilya >> nomer_avtomobilya;
  }

  return summa_shtrafov;
}

bool detect_nachalnik(std::string nomer_avtomobilya)
{
  return nomer_avtomobilya == "A999AA";
}

int poschitat_shtraf(std::string nomer_avtomobilya)
{
  if (krutoj_nomer(nomer_avtomobilya))
    return 1000;
  else if (krasivyj_nomer(nomer_avtomobilya))
    return 500;
  else
    return 100;
}

bool krutoj_nomer(std::string nomer_avtomobilya)
{
  if (nomer_avtomobilya[1] == nomer_avtomobilya[2]
    && nomer_avtomobilya[1] == nomer_avtomobilya[3])
    return true;

  return false;
}

bool krasivyj_nomer(std::string nomer_avtomobilya)
{
  if (nomer_avtomobilya[1] == nomer_avtomobilya[2]
    || nomer_avtomobilya[2] == nomer_avtomobilya[3]
    || nomer_avtomobilya[1] == nomer_avtomobilya[3])
    return true;

    return false;
}

void SortArray(int array[], const int size)
{
    int tmp;
    for (int i = 0; i < size - 1; ++i)
    {
        for (int j = 0; j < size - 1; ++j)
        {
            if (array[j + 1] < array[j])
            {
                tmp = array[j + 1];
                array[j + 1] = array[j];
                array[j] = tmp;
            }
        }
    }

    return;
}

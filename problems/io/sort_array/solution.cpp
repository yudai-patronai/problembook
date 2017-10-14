void SortArray(int arr[], const int size)
{
	int tmp;
	for(int i = 0; i < size - 1; ++i) 
	{            
	    for(int j = 0; j < size - 1; ++j)
	    {     
	        if (arr[j + 1] < arr[j]) 
	        {
	            tmp = arr[j + 1]; 
		        arr[j + 1] = arr[j]; 
	            arr[j] = tmp;
	        }
	    }
	}
	
	return;
}

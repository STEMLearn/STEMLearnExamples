int main()
{
    // step 1: creating some data
    float first_data = 2.2, second_data = 2.4, temp = 0;
    
    // step 2: declaring pointers to reference data
    float *first_data_ptr = &first_data;
    float *second_data_ptr = &second_data;
    
    // step 3: show double pointer just for fun
    float **ptr_to_first_data_ptr = &first_data_ptr;
    
    /** step 4,5,6: swapping first_data, second_data using their pointers */
    temp = *first_data_ptr;
    *first_data_ptr = *second_data_ptr;
    *second_data_ptr = temp;
}
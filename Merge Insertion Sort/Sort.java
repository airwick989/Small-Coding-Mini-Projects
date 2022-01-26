import java.util.Arrays;
import java.util.List;

class Sort
{
    public static final int MAX_CONSTRAINT = 10000000;

    public static long merge(List<Integer> arr, int start, int middle, int end){
        long shifts = 0;
        int first_half = middle - start + 1;
        int second_half = end - middle;

        int left_array[] = new int[first_half + 1];
        int right_array[] = new int[second_half + 1];

        for(int index = 0; index < first_half; index++){
            left_array[index] = arr.get(start + index - 1);
        }
        for(int index = 0; index < second_half; index++){
            right_array[index] = arr.get(middle + index);
        }

        left_array[first_half] = MAX_CONSTRAINT;
        right_array[second_half] = MAX_CONSTRAINT;

        int left_index = 0;
        int right_index = 0;

        for(int merged_index = start - 1; merged_index < end; merged_index++){
            if(left_array[left_index] <= right_array[right_index]){
                arr.set(merged_index, left_array[left_index]);
                left_index ++;
            }
            else{
                arr.set(merged_index, right_array[right_index]);
                right_index ++;

                shifts += first_half - left_index;
            }
        }

        return shifts;
    }

    public static long MergeInsertionSort(List<Integer> arr, int start, int end){

        long shifts = 0;

        if (start < end) {
            int middle = start + (end - start) / 2;
            shifts += MergeInsertionSort(arr, start, middle);
            shifts += MergeInsertionSort(arr, middle + 1, end);
            shifts += merge(arr, start, middle, end);
        }

        return shifts;
    }

    public static void main(String args[])
    {
        List<Integer> arr= Arrays.asList(2, 1, 3, 1, 2);
        System.out.println(MergeInsertionSort(arr, 1, arr.size()));
    }
}
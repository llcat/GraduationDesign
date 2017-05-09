package newfutures;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.function.Consumer;

/**
 * Created by ypl on 17-4-27.
 */
public class TestNewFutures {

    public static void test1(){
        List<Integer> iList = Arrays.asList(3,1,2,5,6);
        List<Integer> i = new ArrayList<Integer>();
        iList.forEach(new Consumer<Integer>() {
            @Override
            public void accept(Integer integer) {
                i.add(integer);
            }
        }

        );
        for(Integer ii : i){
            System.out.println(ii);
        }
    }

    public static void main(String[] args){
        test1();
    }
}

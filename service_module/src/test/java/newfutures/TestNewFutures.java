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
    public static void test2(){
        List<String> list = new ArrayList<>();
        for(int i=0;i<10;i++){
            list.add(new Integer((i)).toString());
        }
        System.out.println(list.subList(3,5).toString());
    }
    public static void test3(){
        List<String> list = new ArrayList<>();
        for(int i=0;i<10;i++){
            list.add(new Integer((i)).toString());
        }
        String s = list.get(1)+list.get(2);
        System.out.println("s:"+s);
        System.out.println("list:"+list.toString());
    }
    public static void main(String[] args){
        //test1();
        test3();
    }
}

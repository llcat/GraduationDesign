package dto;

/**
 * Created by ypl on 17-4-30.
 */

//人工分类标签
public class Tag {


    private String name = "";
    private int count =0;

    public Tag(String name,int count){
        this.name = name;
        this.count = count;
    }
    public String getName() {
        return name;
    }

    public int getCount() {
        return count;
    }

    public void setName(String name) {
        this.name = name;
    }

    public void setCount(int count) {
        this.count = count;
    }

    @Override
    public String toString() {
        return name+": "+count;
    }
}

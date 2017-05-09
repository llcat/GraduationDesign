package dto;

/**
 * Created by ypl on 17-4-30.
 */
public class QueryResult<T> {

    private boolean success;
    private T data;
    private String errorinfo;

    //Controller执行成功返回需要的信息和标示。
    public QueryResult(boolean success, T data) {
        super();
        this.success = success;
        this.data = data;
    }
    //执行失败返回错误信息
    public QueryResult(boolean success, String errorinfo) {
        super();
        this.success = success;
        this.errorinfo = errorinfo;
    }
    /**
     * @return the success
     */
    public boolean isSuccess() {
        return success;
    }
    /**
     * @param success the success to set
     */
    public void setSuccess(boolean success) {
        this.success = success;
    }
    /**
     * @return the data
     */
    public T getData() {
        return data;
    }
    /**
     * @param data the data to set
     */
    public void setData(T data) {
        this.data = data;
    }
    /**
     * @return the errorinfo
     */
    public String getErrorinfo() {
        return errorinfo;
    }
    /**
     * @param errorinfo the errorinfo to set
     */
    public void setErrorinfo(String errorinfo) {
        this.errorinfo = errorinfo;
    }
}

package dao;

import com.mongodb.BasicDBObject;
import com.mongodb.client.FindIterable;
import com.mongodb.client.MongoCollection;
import org.bson.Document;
import static com.mongodb.client.model.Filters.*;

import java.util.*;

/**
 * Created by ypl on 17-4-26.
 */
public class LemmaContentsDaoImpl implements LemmaContentsDAO{
    MongoDBUitl util = new MongoDBUitl();
    private MongoCollection lemmaContentsColl = util.getColl("lemma_contents");

    public List<String> getHotLemma(int top) {

        FindIterable<Document> result= lemmaContentsColl
                .find(gt("history_view_count",10000000))
                .projection(
                        new BasicDBObject("lemma_title",1)
                                .append("history_view_count",1)
                                .append("_id",0)
                )
                .sort(new BasicDBObject("history_view_count",-1))
                .limit(top);
        List<String> re = new ArrayList<String>();
        for(Document doc:result){
            re.add(doc.toJson());
        }
        return re;
    }

    public List<String> getAllTags() {
        FindIterable<Document> iter=lemmaContentsColl.find().projection(new BasicDBObject("lemma_tags",1).append("_id",0));
        int count = 0;
        Map<String,Integer> tagmap = new HashMap<String, Integer>();
        for(Document b:iter){
            ArrayList<String> l = (ArrayList<String>)b.get("lemma_tags");
            for(String s:l){
                if(tagmap.containsKey(s)){
                    tagmap.put(s,tagmap.get(s)+1);
                }else{
                    tagmap.put(s,1);
                }
            }
        }
        for(Map.Entry<String,Integer> o:tagmap.entrySet()){
            System.out.println(o.getKey()+","+o.getValue());
        }
        System.out.print(tagmap.entrySet().size());
        return null;
    }

    public List<String> getKeyInFreqWords(String key) {
        return null;
    }

    public List<String> getKeyInTags(String key) {
        return null;
    }

    public List<String> getLikeTop(int top) {
        return null;
    }

    public List<String> getShareTop(int top) {
        return null;
    }


    public long getCollCount() {
        return lemmaContentsColl.count();
    }

    public static void main(String[] args){
        //测试能否连接
        LemmaContentsDaoImpl lemmaDao = new LemmaContentsDaoImpl();
        long count = lemmaDao.getCollCount();
        System.out.println(count);
//        List<String> r = lemmaDao.getHotLemma(100);
//        for(String s:r){
//            System.out.println(s);
//        }
        lemmaDao.getAllTags();
    }
}

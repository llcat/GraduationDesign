package dao;

import com.mongodb.BasicDBObject;
import com.mongodb.Block;
import com.mongodb.client.FindIterable;
import com.mongodb.client.MongoCollection;
import org.bson.BsonDocument;
import org.bson.Document;
import org.bson.codecs.configuration.CodecRegistry;
import org.bson.conversions.Bson;
import org.springframework.stereotype.Component;

import javax.print.Doc;

import static com.mongodb.client.model.Filters.*;

import java.util.*;

import java.util.function.BiConsumer;
import java.util.function.Consumer;

/**
 * Created by ypl on 17-4-26.
 */
@Component
public class LemmaContentsDaoImpl implements LemmaContentsDAO{
    MongoDBUitl util = new MongoDBUitl();

    private MongoCollection lemmaContentsColl = util.getColl("lemma_contents");

    Block<Document> printBlock = new Block<Document>() {

        public void apply(Document document) {
            System.out.println(document.toJson());
        }
    };

    public List<String> getHotLemma(int top) {

        FindIterable<Document> result= lemmaContentsColl
                .find(gt("history_view_count",10000000))
                .projection(
                        new BasicDBObject("lemma_title",1)
                                .append("history_view_count",1)
                                .append("share_count",1)
                                .append("like_count",1)
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

    public Map<String, Integer> getAllTags() {
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
        return tagmap;
    }

    public List<String> getKeyInFreqWords(String key) {
        return null;
    }

    public List<String> getKeyInTags(String key) {
        FindIterable<Document> iter = lemmaContentsColl.find(new Document("lemma_tags",key)).projection(new Document("lemma_paras",0).append("_id",0));
        List<String> result = new ArrayList<>();
        for(Document d : iter){
            result.add(d.toJson());
        }
        return result;
    }

    public List<String> getLikeTop(int top) {
        FindIterable<Document> iter = lemmaContentsColl.find().projection(new Document("lemma_title",1).append("lemma_id",1).append("like_count",1).append("_id",0)).sort(new Document("like_count",-1)).limit(top);

        //iter.forEach(printBlock);
        List<String> result = new ArrayList<>();
        for(Document doc:iter){
            result.add(doc.toJson());
        }
        return result;
    }

    public List<String> getShareTop(int top) {
        FindIterable<Document> iter = lemmaContentsColl.find().projection(new Document("lemma_title",1).append("lemma_id",1).append("share_count",1).append("_id",0)).sort(new Document("share_count",-1)).limit(top);

        iter.forEach(printBlock);
        List<String> result = new ArrayList<>();
        for(Document doc:iter){
            result.add(doc.toJson());
        }
        return result;
    }

    @Override
    public List<String> getLemmaByKey(String key) {
        FindIterable<Document> iter = lemmaContentsColl.find(new Document("lemma_title",key)).projection(new Document("_id",0).append("lemma_paras",0));
        List<String> result = new ArrayList<>();
        for(Document doc:iter){
            result.add(doc.toJson());
        }
        return result;
    }

    public long getCollCount() {
        return lemmaContentsColl.count();
    }

    public static void main(String[] args){
        //测试能否连接
        LemmaContentsDaoImpl lemmaDao = new LemmaContentsDaoImpl();
        long count = lemmaDao.getCollCount();
        System.out.println(count);
        Consumer<String> consumer = new Consumer<String>() {
            @Override
            public void accept(String s) {
                System.out.println(s);
            }
        };
        //List<String> r = lemmaDao.getHotLemma(100);
        //List<String> r =lemmaDao.getKeyInTags("语言");
        //lemmaDao.getLikeTop(50);
        //lemmaDao.getShareTop(50);
        List<String> r = lemmaDao.getLemmaByKey("人物");
        r.forEach(consumer);
//        Map<String,Integer> m = lemmaDao.getAllTags();
//        for(Map.Entry<String,Integer> e:m.entrySet()){
//            System.out.println(e.getKey()+": "+e.getValue());
//        }
//        System.out.print(m.entrySet().size());
    }

}

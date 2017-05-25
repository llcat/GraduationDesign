package dao;

import com.mongodb.BasicDBObject;
import com.mongodb.Block;
import com.mongodb.Cursor;
import com.mongodb.Mongo;
import com.mongodb.client.FindIterable;
import com.mongodb.client.MongoCollection;
import com.mongodb.client.MongoCursor;
import entity.Lemma;
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

    private MongoCollection relatedInfosColl = util.getColl("related_infos");

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

    public List<Lemma> getKeyInTags(String key) {
        FindIterable<Document> iter = lemmaContentsColl.find(new Document("lemma_tags",key)).projection(new Document("_id",0).append("lemma_id",1).append("lemma_title",1).append("like_count",1).append("share_count",1).append("history_view_count",1).append("history_edit_count",1));
        System.out.println("qurey by tag is ok");
        MongoCursor<Document> cursor = iter.iterator();
        List<Lemma> result = new ArrayList<>();
        int count = 0;
        while(cursor.hasNext()){
            Document d = cursor.tryNext();
            if(d!=null){
                try {
                    Integer id = d.getInteger("lemma_id");
                    String title = d.getString("lemma_title");
                    int viewCount = d.getInteger("history_view_count");
                    int like = d.getInteger("like_count");
                    int share = d.getInteger("share_count");
                    int edit = Integer.parseInt(d.getString("history_edit_count"));
                    Lemma lemma = new Lemma(id, title, viewCount, like, share, edit);
                    result.add(lemma);
                }catch (Exception e){
                    System.out.println("lemma_id:"+d.get("lemma_id")+"\nlemma_like:"+d.get("like_count")+"\nshare:"+d.get("share_count")+"\nedit:"+d.get("edit_count:")+e);
                }
            }

        }
//        for(Document d : iter){
//            result.add(d.toJson());
//        }

//        try {
//            iter.forEach(new Consumer<Document>() {
//                private int count = 1;
//
//                @Override
//                public void accept(Document document) {
//                    count += 1;
//                    System.out.println("for each count" + count);
//                    result.add(document.toJson());
//                }
//            });
//        }catch (Exception e){
//            System.out.println(e);
//        }
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

    @Override
    public Lemma getLemmaById(int id) {
        Lemma lemma = new Lemma();
        FindIterable<Document> iter = lemmaContentsColl.find(new Document("lemma_id",id)).projection(new Document("_id",0).append("lemma_id",1).append("lemma_title",1).append("like_count",1).append("share_count",1).append("history_view_count",1).append("history_edit_count",1));
        for(Document d:iter){
            try {
                Integer id_m = d.getInteger("lemma_id");
                String title = d.getString("lemma_title");
                int viewCount = d.getInteger("history_view_count");
                int like = d.getInteger("like_count");
                int share = d.getInteger("share_count");
                int edit = Integer.parseInt(d.getString("history_edit_count"));
                lemma = new Lemma(id_m, title, viewCount, like, share, edit);
            }catch (Exception e){
                System.out.println("lemma_id:"+d.get("lemma_id")+"\nlemma_like:"+d.get("like_count")+"\nshare:"+d.get("share_count")+"\nedit:"+d.get("edit_count:")+e);
            }
        }
        return lemma;
    }

    @Override
    public List<Integer> getIdBeyKey(String key) {
       FindIterable<Document> iter = lemmaContentsColl.find(new Document("lemma_title",key)).projection(new Document("lemma_id",1));
       List<Integer> re = new ArrayList<>();
       for(Document d:iter){
           try {
               re.add((Integer) (d.get("lemma_id")));
           }catch (Exception e){
               System.out.println(e);
           }
       }
       return re;
    }

    @Override
    public Set<Integer> getAreaByIdList(List<Integer> idList) {
        Set<Integer> re = new HashSet<>();
        for(int i=0;i<idList.size();i++){
            int id = idList.get(i);
            try{
                FindIterable<Document> iter = relatedInfosColl.find(new Document("lemma_id",id)).projection(new Document("_id",0).append("area",1));
                for (Document d : iter){
                    List<List<Integer>> area = (List<List<Integer>>)d.get("area");
                    for (List<Integer> l : area){
                        re.add(l.get(0));
                    }
                }
            }catch(Exception e){
                System.out.println(e);
            }
        }
        return re;
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
//        List<String> r = lemmaDao.getLemmaByKey("人物");
//        r.forEach(consumer);
//        Map<String,Integer> m = lemmaDao.getAllTags();
//        for(Map.Entry<String,Integer> e:m.entrySet()){
//            System.out.println(e.getKey()+": "+e.getValue());
//        }
//        System.out.print(m.entrySet().size());
        //lemmaDao.getIdBeyKey("人物");
        lemmaDao.getAreaByIdList(lemmaDao.getIdBeyKey("人物"));
    }

}

// db.lemma_contents.find({'lemma_tags':'人物'}).sort({'history_view_count':-1}).explain()
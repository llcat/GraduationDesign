package dao;

import com.mongodb.MongoClient;
import com.mongodb.client.FindIterable;
import com.mongodb.client.MongoCollection;
import com.mongodb.client.MongoDatabase;
import org.apache.commons.logging.LogFactory;
import org.apache.commons.logging.Log;
import org.bson.Document;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * Created by ypl on 17-4-26.
 */
public class MongoDBUitl {

    private MongoClient client;
    private MongoDatabase mydb;
    private Log logger = LogFactory.getLog(this.getClass());
    private List<String> existedColl;

    public MongoDBUitl() {
        client = new MongoClient("localhost");
        mydb = client.getDatabase("spider_module_data");
        existedColl = new ArrayList<String>();
        existedColl.add("lemma_contents");
        existedColl.add("old_uls");
        existedColl.add("new_urls");
        existedColl.add("related_infos");
    }

    public MongoCollection getColl(String collName) {
        if (existedColl.contains(collName)) {
            return mydb.getCollection(collName);
        } else {
            logger.info("new coll " + collName);
            return mydb.getCollection(collName);
        }

    }

    public static void ChangeType() {
        MongoDBUitl util = new MongoDBUitl();
        MongoCollection coll = util.getColl("lemma_contents");
        FindIterable<Document> iter = coll.find().projection(new Document("_id", 0).append("lemma_paras", 0));
        for (Document doc : iter) {
            Map<String, Object> up = new HashMap<String, Object>();
            if (doc.get("lemma_id") instanceof String) {
                up.put("lemma_id", Integer.parseInt(doc.getString("lemma_id")));
            } else {
                up.put("lemma_id", doc.get("lemma_id"));
            }
            if (doc.get("like_count") instanceof String) {
                up.put("like_count", Integer.parseInt(doc.getString("like_count")));
            } else {
                up.put("like_count", doc.get("like_count"));
            }
            if (doc.get("share_count") instanceof String) {
                up.put("share_count", Integer.parseInt(doc.getString("share_count")));
            } else {
                up.put("share_count", doc.get("share_count"));
            }

           coll.updateOne(new Document("lemma_id", doc.get("lemma_id")), new Document("$set", new Document(up)));
            //System.out.println(up.toString());
        }
    }

    public static void main(String[] args) {
        ChangeType();
    }
}

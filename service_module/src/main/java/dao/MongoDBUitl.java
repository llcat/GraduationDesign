package dao;
import com.mongodb.MongoClient;
import com.mongodb.client.MongoCollection;
import com.mongodb.client.MongoDatabase;
import org.apache.commons.logging.LogFactory;
import org.apache.commons.logging.Log;

import java.util.ArrayList;
import java.util.List;

/**
 * Created by ypl on 17-4-26.
 */
public class MongoDBUitl {

    private MongoClient client;
    private MongoDatabase mydb;
    private Log logger = LogFactory.getLog(this.getClass());
    private List<String> existedColl;
    public MongoDBUitl(){
        client = new MongoClient("localhost");
        mydb = client.getDatabase("spider_module_data");
        existedColl = new ArrayList<String>();
        existedColl.add("lemma_contents");
        existedColl.add("old_uls");
        existedColl.add("new_urls");
    }

    public MongoCollection getColl(String collName){
        if(existedColl.contains(collName)){
            return mydb.getCollection(collName);
        }else{
            logger.info("new coll "+collName);
            return mydb.getCollection(collName);
        }

    }

}

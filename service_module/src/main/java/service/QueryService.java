package service;

import dao.LemmaContentsDAO;
import dto.QueryResult;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * Created by ypl on 17-4-27.
 */

@Service
public class QueryService {
    private LemmaContentsDAO lemmaDao;

    @Autowired
    public QueryService(LemmaContentsDAO dao){
        lemmaDao = dao;
    }

    public List<String> queryByKey(String key){
        List<String> byKey = lemmaDao.getLemmaByKey(key);
        return byKey;
    }

    public List<String> queryInTags(String key){
        List<String> keyInTags = lemmaDao.getKeyInTags(key);
        if(keyInTags.size()>20){
            return keyInTags.subList(0,20);
        }else {
            return keyInTags;
        }
    }
}

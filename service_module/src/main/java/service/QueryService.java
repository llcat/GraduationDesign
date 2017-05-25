package service;

import dao.LemmaContentsDAO;
import dto.QueryResult;
import entity.Lemma;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.*;
import java.lang.System;

/**
 * Created by ypl on 17-4-27.
 */

@Service
public class QueryService {
    private LemmaContentsDAO lemmaDao;
    private Map<String,List<Lemma>> cacheTag = new HashMap();
    private Map<String,List<Lemma>> cacheCluster = new HashMap();
    @Autowired
    public QueryService(LemmaContentsDAO dao){
        lemmaDao = dao;
    }

    public List<String> queryByKey(String key){
        long start = System.nanoTime();
        List<String> byKey = lemmaDao.getLemmaByKey(key);
        long end = System.nanoTime();
        System.out.println("in qurey by tags cost time:"+(end-start));
        return byKey;
    }

    public QueryResult<List<Lemma>> queryInTags(String key,int page){
        System.out.println("in query by tags service.....");
        if(page<1){
            page = 1;
        }
        int start = (page-1)*10;
        int end = (page)*10;
        if(cacheTag.get(key) != null){
            List<Lemma> list = cacheTag.get(key);
            if(start>=list.size()-1){
                start = 0;
                end = 0;
            }
            if(end>list.size()){
                end = list.size();
            }
            QueryResult<List<Lemma>> re = new QueryResult<List<Lemma>>(true,list.subList(start,end),list.size());
            return re;
        }
        List<Lemma> keyInTags = lemmaDao.getKeyInTags(key);
        keyInTags.sort(new Comparator<Lemma>() {
            @Override
            public int compare(Lemma o1, Lemma o2) {
                return o2.getHistoryViewCount() - o1.getHistoryViewCount();
            }
        });
        cacheTag.put(key,keyInTags);
        if(start>=keyInTags.size()-1){
            start = 0;
            end = 0;
        }
        if(end>keyInTags.size()){
            end = keyInTags.size();
        }
        QueryResult<List<Lemma>> re = new QueryResult<List<Lemma>>(true,keyInTags.subList(start,end),keyInTags.size());
        return re;
    }

    //给出某个词条的聚类的聚类结果
    public QueryResult<List<Lemma>> queryByCluster(String key,int page){

        List<Lemma> data = new ArrayList<>();
        if(page<1){
            page = 1;
        }
        int start = (page-1)*10;
        int end = (page)*10;
        if(cacheCluster.get(key)!=null){
            List<Lemma> d = cacheCluster.get(key);
            if(start>=d.size()-1){
                start = 0;
                end = 0;
            }
            if(end>d.size()){
                end = d.size();
            }
            return new QueryResult<List<Lemma>>(true,d.subList(start,end),d.size());
        }
        //1. 取得相关键值的所有id
        Set<Integer> area =  lemmaDao.getAreaByIdList(lemmaDao.getIdBeyKey(key));
        //2. 根据id值查询所有的lemma
        for(Integer id:area){
            try {
                Lemma lemma = lemmaDao.getLemmaById(id);
                data.add(lemma);
            }catch (Exception e){
                System.out.println(e);
            }
        }
        cacheCluster.put(key,data);
        if(start>=data.size()-1){
            start = 0;
            end = 0;
        }
        if(end>data.size()){
            end = data.size();
        }
        return new QueryResult<List<Lemma>>(true,data.subList(start,end),data.size());
    }
}

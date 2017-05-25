package dao;

import entity.Lemma;

import java.util.List;
import java.util.Map;
import java.util.Set;

/**
 * Created by ypl on 17-4-26.
 */
public interface LemmaContentsDAO {

    //返回浏览量前top的词条
    List<String> getHotLemma(int top);

    //返回喜欢数前top的词条
    List<String> getLikeTop(int top);

    //返回分享数前top的词条
    List<String> getShareTop(int top);

    //返回关键字在tags中的词条
    List<Lemma> getKeyInTags(String key);

    //返回关键字在提取的高频词中的词条
    List<String> getKeyInFreqWords(String key);

    //返回暂时采集数据的所有分类
    Map<String,Integer> getAllTags();

    List<String> getLemmaByKey(String key);
    long getCollCount();

    //根据键值查询相关词条词条id
    List<Integer> getIdBeyKey(String key);

    //根据id查找词条的领域相关的点
    Lemma getLemmaById(int id);

    //根据一组id取得所有的领域点id,去重
    Set<Integer> getAreaByIdList(List<Integer> idList);

}

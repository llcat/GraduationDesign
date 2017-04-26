package dao;

import entity.Lemma;

import java.util.List;

/**
 * Created by ypl on 17-4-26.
 */
public interface LemmaContentsDAO {

    //返回浏览量前top的词条
    public List<String> getHotLemma(int top);

    //返回喜欢数前top的词条
    public List<String> getLikeTop(int top);

    //返回分享数前top的词条
    public List<String> getShareTop(int top);

    //返回关键字在tags中的词条
    public List<String> getKeyInTags(String key);

    //返回关键字在提取的高频词中的词条
    public List<String> getKeyInFreqWords(String key);

    //返回暂时采集数据的所有分类
    public List<String> getAllTags();

    public long getCollCount();
}
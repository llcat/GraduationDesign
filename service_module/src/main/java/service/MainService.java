package service;

import dao.LemmaContentsDAO;
import dao.LemmaContentsDaoImpl;
import dto.Tag;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import javax.swing.text.html.parser.Entity;
import java.util.*;

/**
 * Created by ypl on 17-4-30.
 */
@Service
public class MainService {

    private LemmaContentsDAO lemmaDao;
    private Map<String,List<Tag>> cache= new HashMap<String,List<Tag>>();

    @Autowired
    public MainService(LemmaContentsDAO dao){
        lemmaDao = dao;
    }

    public List<String> getHotLemma(int top){
        return lemmaDao.getHotLemma(top);
    }

    public List<Tag> getHotTags(int top){
        if(cache.get("hotTags")!=null){
            List<Tag> tagList = cache.get("hotTags");
            return tagList.subList(0,top);
        }
        List<Tag> re = new ArrayList<>();
        Map<String,Integer> map = lemmaDao.getAllTags();
        List<Map.Entry<String,Integer>> tempList = new ArrayList(map.entrySet());
        Collections.sort(tempList, new Comparator<Map.Entry<String,Integer>>() {
            @Override
            public int compare(Map.Entry<String, Integer> o1, Map.Entry<String, Integer> o2) {
                return o2.getValue()-o1.getValue();
            }
        });
        int other = 0;
        for(Map.Entry<String,Integer> e:tempList){
            String name = e.getKey();
            int count = e.getValue();
            Tag tag = new Tag(name,count);
            re.add(tag);
        }
        cache.put("hotTags",re);
        return re.subList(0,top);
    }

    public static void main(String[] args){
        MainService ms = new MainService(new LemmaContentsDaoImpl());
        List<Tag> l = ms.getHotTags(20);
        System.out.print(l.size());
        for(Tag t:l){
            System.out.println(t.toString());
        }
    }
}

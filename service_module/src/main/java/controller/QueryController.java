package controller;

import dto.QueryResult;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseBody;
import service.QueryService;

import java.util.List;
import java.util.Map;

/**
 * Created by ypl on 17-5-2.
 */

@Controller
@RequestMapping("")
public class QueryController {
    @Autowired
    private QueryService queryService;

    @RequestMapping("/result-list/{keyword}")
    public String list(@PathVariable("keyword") String keyword, Model model){
        System.out.println("取得请求");
        model.addAttribute("keyword",keyword);
        return "search";
    }

    @RequestMapping(value = "/search/{key}",produces = "application/json ;charset=UTF-8")
    @ResponseBody
    public String search(@PathVariable("key")String key){
        System.out.println("search a key");
        return queryService.queryByKey(key).toString();
    }

    @RequestMapping(value = "/searchInTags/{key}",produces = "application/json ;charset=UTF-8")
    @ResponseBody
    public String searchInTags(@PathVariable("key")String key){
        return queryService.queryInTags(key).toString();
    }

    @RequestMapping("/{lemma}/detail")
    public String detail(@PathVariable("lemma") String lemma,Model model){
        System.out.println(lemma);
        return "detail";
    }

}

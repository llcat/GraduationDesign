package controller;

import dto.QueryResult;
import dto.Tag;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.portlet.ModelAndView;
import service.MainService;

import java.util.Date;
import java.util.List;

/**
 * Created by ypl on 17-4-27.
 * 暂定页面为3个
 * home,search,detail页
 * 除了几个页面的跳转，其他
 * 前后端交互基于Restful API完成
 *
 */


@Controller
@RequestMapping("")
public class MainPageController {

    @Autowired
    private MainService mainService;

    @RequestMapping(value = "/",method = RequestMethod.GET)
    public String home(Model model){
        System.out.println("get a rquest");
        return "home";
    }
    @RequestMapping(value = "/topview",produces = "application/json;charset=UTF-8")
    @ResponseBody
    public String topViewLemmas(){
        System.out.println("get top view......");
        List<String> re = mainService.getHotLemma(50);
        System.out.println(re.toString());
        return re.toString();
    }
    @RequestMapping(value = "/hottags/{top}",produces = "application/json;charset=UTF-8")
    @ResponseBody
    public List<Tag> hotTags(@PathVariable("top") int top){

        System.out.println("get hotTags......"+top);
        List<Tag> re = mainService.getHotTags(top);
        return re;
    }

    @RequestMapping(value = "/now",produces = "application/json;charset=UTF-8")
    @ResponseBody
    public QueryResult<Date> now(){
        System.out.println("get host time....");
        Date now = new Date();
        return new QueryResult<Date>(true, now);
    }


}

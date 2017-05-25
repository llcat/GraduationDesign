package entity;

/**
 * Created by ypl on 17-4-26.
 */
public class Lemma {
    private int lemmaId;
    private String LemmaTitle;
    private String lemmaParas;
    private String lemmaCreator;
    private int historyViewCount;
    private int likeCount;

    public Lemma(){}
    public Lemma(int lemmaId, String lemmaTitle, int historyViewCount, int likeCount, int shareCount, int editCount) {
        this.lemmaId = lemmaId;
        LemmaTitle = lemmaTitle;
        this.historyViewCount = historyViewCount;
        this.likeCount = likeCount;
        this.shareCount = shareCount;
        this.editCount = editCount;
    }

    public int getLemmaId() {
        return lemmaId;
    }

    public void setLemmaId(int lemmaId) {
        this.lemmaId = lemmaId;
    }

    public String getLemmaTitle() {
        return LemmaTitle;
    }

    public void setLemmaTitle(String lemmaTitle) {
        LemmaTitle = lemmaTitle;
    }

    public String getLemmaParas() {
        return lemmaParas;
    }

    public void setLemmaParas(String lemmaParas) {
        this.lemmaParas = lemmaParas;
    }

    public String getLemmaCreator() {
        return lemmaCreator;
    }

    public void setLemmaCreator(String lemmaCreator) {
        this.lemmaCreator = lemmaCreator;
    }

    public int getHistoryViewCount() {
        return historyViewCount;
    }

    public void setHistoryViewCount(int historyViewCount) {
        this.historyViewCount = historyViewCount;
    }

    public int getLikeCount() {
        return likeCount;
    }

    public void setLikeCount(int likeCount) {
        this.likeCount = likeCount;
    }

    public int getShareCount() {
        return shareCount;
    }

    public void setShareCount(int shareCount) {
        this.shareCount = shareCount;
    }

    public String[] getLemmaTags() {
        return lemmaTags;
    }

    public void setLemmaTags(String[] lemmaTags) {
        this.lemmaTags = lemmaTags;
    }

    public int getEditCount() {
        return editCount;
    }

    public void setEditCount(int editCount) {
        this.editCount = editCount;
    }

    private int shareCount;
    private String[] lemmaTags;
    private int editCount;

}

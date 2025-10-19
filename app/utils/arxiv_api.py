#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2024/9/21 23:07
# @Author : 桐
# @QQ:1041264242
# 注意事项：
import arxiv
import json


def get_authors(authors, first_author=False):
    if not first_author:
        output = ", ".join(str(author) for author in authors)
    else:
        output = authors[0]
    return output


def get_papers(query="astronomy", max_results=2):
    """
    @param topic: str
    @param query: str
    @return paper_with_code: dict
    """

    paper_list = []

    search_engine = arxiv.Search(
        query=query,
        max_results=max_results,
        sort_by=arxiv.SortCriterion.Relevance
    )

    for result in search_engine.results():
        paper_id = result.entry_id
        paper_title = result.title
        paper_pdf = result.pdf_url
        paper_doi = result.doi
        paper_abstract = result.summary.replace("\n", " ")
        paper_authors = get_authors(result.authors)
        primary_category = result.primary_category
        publish_time = result.published.date().isoformat()

        data = {"topic": query,
                "title": paper_title,
                "id": paper_id,
                "doi": paper_doi,
                "pdf": paper_pdf,
                "abstract": paper_abstract,
                "authors": paper_authors,
                "category": primary_category,
                "time": publish_time}

        paper_list.append(data)

    return paper_list


def search_paper(Keywords, Limit=2):
    data_collector = []

    for keyword in Keywords:
        print(f"Info: retrieve papers related to technical entities...")
        data_collector += get_papers(query=keyword, max_results=Limit)
        print(json.dumps(data_collector, indent=4))
        print(f"Info: retrieve papers related to technical entities: {keyword} State:OK!")
    return data_collector

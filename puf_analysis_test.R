library(survey)
library(tidyverse)
library(dplyr)
library(ggplot2)
library(data.table)
`%nin%` <- Negate(`%in%`)

setwd("/Users/yehyland/iCloud Drive (Archive)/Desktop/RPK/githublink/y2025/y2025")

df <- read.csv("APNORC_june2021_PUF.csv")

methodological <- c("SU_ID","FINALWT")
variables <- c("POLITICS","DEMO","REPUB","INDEP","IDEO","URBAN","MARITAL","AGEGRP","EDUCATION","RACETH","GENDER","HHINCOME","EMPSTATUS","CENSUS_REGION","SURV_MODE","SURV_LANG")
questions <- colnames(df)[!(colnames(df) %in% variables)&!(colnames(df) %in% methodological)&colnames(df)!="STATE"]

question <- c("CURY2D")

lapply(question,function(question) {
  
    for (varx in variables) {
      print(varx)
      print(
        ggplot(df, aes(fill=df[[question]], y = FINALWT, x = ifelse(df[[varx]] == toupper(df[[varx]]), "(5) Missing", df[[varx]]))) +
          geom_bar(position = "fill", stat = "identity") +
          theme(axis.text.x = element_text(angle = 90, vjust = 0.5)) +
          #coord_flip() +
          labs(x = paste(varx), y = "PROPORTION", fill = "Response") 
      )
    }
})

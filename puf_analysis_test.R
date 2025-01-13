#install.packages("autumn")

library(tidyverse)
library(dplyr)
library(ggplot2)
library(data.table)

setwd("/Users/yehyland/iCloud Drive (Archive)/Desktop/RPK/githublink/y2025/y2025")

df <- read.csv("APNORC_june2021_PUF.csv")

table(df$CUR1, df$POLITICS)

df$CUR1_by_POL <- paste(df$POLITICS, " - ", df$CUR1)

ggplot(df, aes(fill=CUR1, y = FINALWT, x = ifelse(POLITICS %like% "VOL", "(5) Missing", POLITICS))) +
         geom_bar(position = "fill", stat = "identity") +
          theme(axis.text.x = element_text(angle = 90, vjust = 0.5)) +
  labs(x = "POLITICS", y = "PROPORTION")
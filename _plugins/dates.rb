module Jekyll
    module OrdinalDates
        def ordinalDate(date)
            month = time(date).strftime("%B")
            day = time(date).strftime("%e") # leading zero is replaced by a space
            if day in [1,21,31]
              ordinal = "st"
            elsif day in [2, 22]
              ordinal = "nd"
            elsif day in [3, 23]
              ordinal = "rd"
            else
              ordinal = "th"
            end
            year = time(date).strftime("%Y")
            month+" "+day+"<sup>#{ordinal}</sup> "+year
        end
    end
end

Liquid::Template.register_filter(Jekyll::OrdinalDates)

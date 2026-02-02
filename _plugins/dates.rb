module Jekyll
    module OrdinalDates
        def ordinalDate(date)
            month = time(date).strftime("%B")
            day = time(date).strftime("%e") # leading zero is replaced by a space
            if [" 1","21","31"].include?(day)
              ordinal = "st"
            elsif [" 2","22"].include?(day)
              ordinal = "nd"
            elsif [" 3","23"].include?(day)
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

using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.Linq;
using System.Web;

namespace LibraryApplication.Models
{
    public class Book
    {
        [Key]
        public int BookId { get; set; }
        public string Title { get; set; }
        public string Writer { get; set; }
        public string Summary { get; set; }
        public string Pulisher { get; set; }
        public int Published_date { get; set; }
    }
}